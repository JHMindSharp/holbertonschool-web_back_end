import handleProfileSignup from '../6-final-user.js';

test('handleProfileSignup handles all promises', () => {
  expect.assertions(2);
  return handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg').then(data => {
    expect(data).toEqual([
      { status: 'fulfilled', value: { firstName: 'Bob', lastName: 'Dylan' } },
      { status: 'rejected', value: new Error('bob_dylan.jpg cannot be processed') },
    ]);
  });
});
