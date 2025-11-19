from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from db import SessionLocal, init_db
from models import Review
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)

conversations = {}

STATE_ASK_PRODUCT = "ask_product"
STATE_ASK_NAME = "ask_name"
STATE_ASK_REVIEW = "ask_review"

def make_twiml_message(body):
    response = ET.Element('Response')
    message = ET.SubElement(response, 'Message')
    message.text = body
    return ET.tostring(response, encoding='utf-8')

init_db()

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming = request.form.get("Body", "").strip()
    from_number = request.form.get("From", "").replace("whatsapp:", "").strip()

    conv = conversations.get(from_number, {"state": STATE_ASK_PRODUCT, "data": {}})
    state = conv["state"]
    data = conv["data"]

    if incoming.lower() in ["hi", "hello", "start", "restart"]:
        conversations[from_number] = {"state": STATE_ASK_PRODUCT, "data": {}}
        return Response(make_twiml_message("Which product is this review for?"), mimetype="text/xml")

    if state == STATE_ASK_PRODUCT:
        data["product_name"] = incoming
        conversations[from_number] = {"state": STATE_ASK_NAME, "data": data}
        return Response(make_twiml_message("What's your name?"), mimetype="text/xml")

    if state == STATE_ASK_NAME:
        data["user_name"] = incoming
        conversations[from_number] = {"state": STATE_ASK_REVIEW, "data": data}
        return Response(make_twiml_message(f"Please send your review for {data['product_name']}"), mimetype="text/xml")

    if state == STATE_ASK_REVIEW:
        data["product_review"] = incoming

        db = SessionLocal()
        review = Review(
            contact_number=from_number,
            user_name=data["user_name"],
            product_name=data["product_name"],
            product_review=data["product_review"],
        )
        db.add(review)
        db.commit()
        db.close()

        conversations.pop(from_number, None)

        return Response(make_twiml_message("Thanks! Your review has been saved."), mimetype="text/xml")

    return Response(make_twiml_message("Send 'restart' to try again."), mimetype="text/xml")

@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    db = SessionLocal()
    result = db.query(Review).order_by(Review.created_at.desc()).all()
    db.close()

    return jsonify([
        {
            "id": r.id,
            "contact_number": r.contact_number,
            "product_name": r.product_name,
            "user_name": r.user_name,
            "product_review": r.product_review,
            "created_at": r.created_at.isoformat(),
        }
        for r in result
    ])

if __name__ == "__main__":
    app.run(port=5000, debug=True)