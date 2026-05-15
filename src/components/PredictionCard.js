import { useState } from "react";
import "./PredictionCard.css";

function PredictionCard({ getPrediction }) {
  const [loading, setLoading] = useState(false);
  const [prediction, setPrediction] = useState(null);

  const fetchPrediction = async () => {
    setLoading(true);
    const result = await getPrediction();
    setPrediction(result);
    setLoading(false);
  };

  return (
    <div className="prediction-card">
      {loading ? (
        <div className="loader">
          <div className="spinner"></div>
          <p>Analyzing market trends...</p>
        </div>
      ) : (
        <p>{prediction}</p>
      )}
      <button onClick={fetchPrediction}>Predict</button>
    </div>
  );
}

export default PredictionCard;
