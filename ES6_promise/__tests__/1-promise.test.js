import getFullResponseFromAPI from '../1-promise.js';

test('getFullResponseFromAPI resolves with success', () => {
  expect.assertions(1);
  return getFullResponseFromAPI(true).then(data => {
    expect(data).toEqual({
      status: 200,
      body: 'Success',
    });
  });
});

test('getFullResponseFromAPI rejects with error', () => {
  expect.assertions(1);
  return getFullResponseFromAPI(false).catch(error => {
    expect(error).toEqual(new Error('The fake API is not working currently'));
  });
});
