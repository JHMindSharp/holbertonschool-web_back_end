import handleProfileSignup from '../3-all.js';

test('handleProfileSignup logs correct message on success', () => {
  console.log = jest.fn();
  return handleProfileSignup().then(() => {
    expect(console.log).toHaveBeenCalledWith('photo-profile-1 Guillaume Salva');
  });
});

test('handleProfileSignup logs error message on failure', () => {
  console.log = jest.fn();
  jest.mock('../utils.js', () => ({
    uploadPhoto: jest.fn().mockRejectedValue(new Error('Error')),
    createUser: jest.fn().mockRejectedValue(new Error('Error')),
  }));

  const handleProfileSignup = require('../3-all.js').default;
  return handleProfileSignup().then(() => {
    expect(console.log).toHaveBeenCalledWith('Signup system offline');
  });
});
