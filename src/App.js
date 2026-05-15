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
import PredictionCard from "./components/PredictionCard";

function App() {
  // Example prediction function
  const fetchPredictionFromAPI = async () => {
    // Replace this with your actual API call
    return "Bitcoin will rise 🚀";
  };

  return (
    <div>
      <h1>Crypto Market Predictor</h1>
      <PredictionCard getPrediction={fetchPredictionFromAPI} />
    </div>
  );
}

export default App;

