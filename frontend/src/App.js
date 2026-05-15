import React, { useEffect, useState } from "react";
import PriceDisplay from "./components/PriceDisplay";

function App() {
  const [price, setPrice] = useState(null);

  useEffect(() => {
    fetch("https://crypto-market-predictor.onrender.com/price")
      .then((response) => response.json())
      .then((data) => setPrice(data.price));
  }, []);

  return (
    <div>
      <h1>Crypto Market Predictor</h1>
      {price ? <PriceDisplay price={price} /> : <p>Loading...</p>}
    </div>
  );
}

export default App;
