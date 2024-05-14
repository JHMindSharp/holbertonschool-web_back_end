function uploadPhoto(fileName) {
    return Promise.reject(new Error(`${fileName} cannot be processed`));
  }
  
  module.exports = uploadPhoto;
  