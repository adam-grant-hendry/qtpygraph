module.exports = {
    rules: {
      'header-max-length': [2, 'always', 50], // Subject line must be <= 50 characters
      'header-full-stop': [2, 'never', '.'], // Subject line must not end with a period
      'body-max-line-length': [2, 'always', 80], // Detailed message lines must be <= 80 characters
    },
  };
