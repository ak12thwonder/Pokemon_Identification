const imageInput = document.getElementById('imageInput');
const imagePreview = document.getElementById('imagePreview');
const predictBtn = document.getElementById('predictBtn');
const resultDiv = document.getElementById('result');
const errorDiv = document.getElementById('error');
let selectedFile = null;
    
imageInput.addEventListener('change', function() {
  const file = this.files[0];
  selectedFile = file;
  resultDiv.innerHTML = '';
  errorDiv.textContent = '';
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      imagePreview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
    }
    reader.readAsDataURL(file);
    predictBtn.disabled = false;
  } else {
    imagePreview.innerHTML = '<span>Image Preview</span>';
    predictBtn.disabled = true;
  }
});

predictBtn.addEventListener('click', async function() {
  if (!selectedFile) return;
  errorDiv.textContent = '';
  resultDiv.innerHTML = '';
  predictBtn.disabled = true;
  predictBtn.textContent = 'Predicting...';

  // 1. Send image to /predict
  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const predictRes = await fetch('http://127.0.0.1:8000/predict', {
      method: 'POST',
      body: formData
    });
    if (!predictRes.ok) throw new Error('Prediction failed');
    const predictData = await predictRes.json();
    const species = predictData.species || predictData.prediction || predictData.name;
    if (!species) throw new Error('No species returned from prediction');

    // 2. Fetch stats from /stats/{species}
    const statsRes = await fetch(`http://127.0.0.1:8000/stats/${encodeURIComponent(species)}`);
    if (!statsRes.ok) throw new Error('Stats not found for predicted species');
    const stats = await statsRes.json();

    // 3. Show result
    resultDiv.innerHTML = `
      <div class="result-card">
        <h2>${species}</h2>
        <ul class="stats-list">
          ${Object.entries(stats).map(([key, value]) => `<li><strong>${key}:</strong> ${value}</li>`).join('')}
        </ul>
      </div>
    `;
  } catch (err) {
    errorDiv.textContent = err.message;
  } finally {
    predictBtn.disabled = false;
    predictBtn.textContent = 'Predict';
  }
});