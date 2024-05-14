import getResponseFromAPI from '../0-promise.js';

test('getResponseFromAPI returns a Promise', () => {
  const response = getResponseFromAPI();
  expect(response).toBeInstanceOf(Promise);
});
