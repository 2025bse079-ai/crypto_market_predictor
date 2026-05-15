import React from 'react';

function PriceDisplay({ symbol, price, change }) {
  return (
    <div className="price-display">
      <h2>{symbol}</h2>
      <p>${price}</p>
      <p>{change}%</p>
    </div>
  );
}

export default PriceDisplay;