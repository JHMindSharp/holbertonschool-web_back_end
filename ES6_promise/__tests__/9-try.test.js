import guardrail from '../9-try.js';
import divideFunction from '../8-try.js';

test('guardrail returns correct output on success', () => {
  const result = guardrail(() => divideFunction(10, 2));
  expect(result).toEqual([5, 'Guardrail was processed']);
});

test('guardrail returns correct output on error', () => {
  const result = guardrail(() => divideFunction(10, 0));
  expect(result).toEqual(['Error: cannot divide by 0', 'Guardrail was processed']);
});
