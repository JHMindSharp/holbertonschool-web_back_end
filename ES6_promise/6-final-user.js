import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

function handleProfileSignup(firstName, lastName, fileName) {
  const signUp = signUpUser(firstName, lastName);
  const upload = uploadPhoto(fileName);

  return Promise.allSettled([signUp, upload]).then((results) => {
    return results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    }));
  });
}

export default handleProfileSignup;
