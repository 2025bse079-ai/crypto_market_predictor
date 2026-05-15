import { useEffect, useState } from "react";
import "./Price.css";

function PriceDisplay({ newPrice }) {
  const [price, setPrice] = useState(newPrice);
  const [flash, setFlash] = useState("");

  useEffect(() => {
    if (newPrice > price) {
      setFlash("flash-green");
    } else if (newPrice < price) {
      setFlash("flash-red");
    }
    setPrice(newPrice);

    const timer = setTimeout(() => setFlash(""), 500);
    return () => clearTimeout(timer);
  }, [newPrice]);

  return <div className={`price ${flash}`}>${price.toFixed(2)}</div>;
}

export default PriceDisplay;
