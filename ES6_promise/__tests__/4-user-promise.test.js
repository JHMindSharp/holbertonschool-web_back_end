import signUpUser from '../4-user-promise.js';

test('signUpUser returns a resolved promise with user details', () => {
  expect.assertions(1);
  return signUpUser('Bob', 'Dylan').then(data => {
    expect(data).toEqual({
      firstName: 'Bob',
      lastName: 'Dylan',
    });
  });
});
