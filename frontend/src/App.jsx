import { useEffect, useState } from "react";

export default function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/reviews")
      .then((res) => res.json())
      .then(setReviews)
      .catch((err) => console.error("Error fetching reviews:", err));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>WhatsApp Product Reviews</h1>

      <table
        border="1"
        cellPadding="10"
        style={{ width: "100%", borderCollapse: "collapse" }}
      >
        <thead>
          <tr>
            <th>User</th>
            <th>Product</th>
            <th>Review</th>
            <th>Contact</th>
            <th>Submitted At</th>
          </tr>
        </thead>

        <tbody>
          {reviews.map((r) => (
            <tr key={r.id}>
              <td>{r.user_name}</td>
              <td>{r.product_name}</td>
              <td>{r.product_review}</td>
              <td>{r.contact_number}</td>
              <td>{new Date(r.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

