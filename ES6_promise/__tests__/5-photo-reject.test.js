import uploadPhoto from '../5-photo-reject.js';

test('uploadPhoto returns a rejected promise with error message', () => {
  expect.assertions(1);
  return uploadPhoto('guillaume.jpg').catch(error => {
    expect(error).toEqual(new Error('guillaume.jpg cannot be processed'));
  });
});
