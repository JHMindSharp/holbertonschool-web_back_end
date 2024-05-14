export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      const fakeResponse = {
        status: 200,
        body: 'Fake response from API',
      };
      resolve(fakeResponse);
    });
  }
  