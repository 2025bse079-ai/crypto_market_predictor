import PriceDisplay from "./components/PriceDisplay";

function App() {
  const cryptoPrice = 120.45; // replace with your live price state

  return (
    <div>
      <h1>Crypto Market Predictor</h1>
      <PriceDisplay newPrice={cryptoPrice} />
    </div>
  );
}

export default App;
