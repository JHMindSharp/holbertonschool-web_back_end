import handleResponseFromAPI from '../2-then.js';

test('handleResponseFromAPI resolves correctly', () => {
  const promise = Promise.resolve();
  handleResponseFromAPI(promise).then((data) => {
    expect(data).toEqual({
      status: 200,
      body: 'success',
    });
  });
});

test('handleResponseFromAPI logs message', () => {
  console.log = jest.fn();
  const promise = Promise.resolve();
  handleResponseFromAPI(promise);
  expect(console.log).toHaveBeenCalledWith('Got a response from the API');
});
