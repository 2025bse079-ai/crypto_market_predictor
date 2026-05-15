import PriceDisplay from "./components/PriceDisplay";
import PredictionCard from "./components/PredictionCard";
import Card from "./components/Card";

function App() {
  const cryptoPrice = 120.45; // replace with your live price state

  // Example prediction function
  const fetchPredictionFromAPI = async () => {
    await new Promise(resolve => setTimeout(resolve, 2000)); // simulate loading
    return "Bitcoin is likely to rise 🚀";
  };

  return (
    <div>
      <h1>Crypto Market Predictor</h1>

      {/* Wrap PriceDisplay inside Card */}
      <Card>
        <PriceDisplay newPrice={cryptoPrice} />
      </Card>

      {/* Wrap PredictionCard inside Card */}
      <Card>
        <PredictionCard getPrediction={fetchPredictionFromAPI} />
      </Card>
    </div>
  );
}

export default App;
