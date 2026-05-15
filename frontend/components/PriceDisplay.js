import React, { useEffect, useState } from "react";

function PriceDisplay() {
  const [prices, setPrices] = useState({});

  useEffect(() => {
    fetch(process.env.REACT_APP_BACKEND_URL + "/prices")
      .then((response) => response.json())
      .then((data) => setPrices(data));
  }, []);

  return (
    <div>
      <h2>Crypto Prices</h2>
      <ul>
        {Object.entries(prices).map(([coin, price]) => (
          <li key={coin}>
            {coin.toUpperCase()}: ${price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PriceDisplay;
