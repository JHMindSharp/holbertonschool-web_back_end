import loadBalancer from '../7-load_balancer.js';

test('loadBalancer returns value of the first resolved promise', () => {
  const promise1 = new Promise((resolve) => setTimeout(resolve, 100, 'First'));
  const promise2 = new Promise((resolve) => setTimeout(resolve, 200, 'Second'));

  expect.assertions(1);
  return loadBalancer(promise1, promise2).then(data => {
    expect(data).toBe('First');
  });
});
