import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState('');
  const [additionalInfo, setAdditionalInfo] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [results, setResults] = useState(null);

  const handleUrlChange = (e) => {
    setUrl(e.target.value);
  };

  const handleAdditionalInfoChange = (e) => {
    setAdditionalInfo(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults(null);

    try {
      const response = await axios.post('/api/scrape', {
        url,
        additional_info: additionalInfo,
      });
      setResults(response.data);
    } catch (err) {
      setError('An error occurred while scraping the website.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Web Scraping Sandbox</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Website URL:
            <input type="text" value={url} onChange={handleUrlChange} required />
          </label>
        </div>
        <div>
          <label>
            Additional Information:
            <input type="text" value={additionalInfo} onChange={handleAdditionalInfoChange} />
          </label>
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Scraping...' : 'Scrape'}
        </button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {results && (
        <div>
          <h2>Scraping Results</h2>
          <p><strong>Title:</strong> {results.title}</p>
          <p><strong>Emails:</strong> {results.emails.join(', ')}</p>
          <p><strong>Phone Numbers:</strong> {results.phone_numbers.join(', ')}</p>
          <p><strong>Cleaned Text Sample:</strong> {results.cleaned_text_sample}</p>
          {results.additional_info && (
            <p><strong>Additional Info:</strong> {results.additional_info}</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
