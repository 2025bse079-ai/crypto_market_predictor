import PredictionCard from "./components/PredictionCard";

function App() {
  // Example prediction function (replace with your real API call)
  const fetchPredictionFromAPI = async () => {
    // Simulate delay for loading animation
    await new Promise(resolve => setTimeout(resolve, 2000));
    return "Bitcoin is likely to rise 🚀"; 
  };

  return (
    <div>
      <h1>Crypto Market Predictor</h1>
      
      {/* Prediction Card with loading animation */}
      <PredictionCard getPrediction={fetchPredictionFromAPI} />
    </div>
  );
}

export default App;
