# React Fundamentals and trticky questions

## Quick checks

### In React, what’s the difference between a controlled input and an uncontrolled input?
Give a short example of each and when you’d prefer one.

- Controlled: value comes from React state; onChange updates state; React is the source of truth.

- Uncontrolled: value lives in the DOM; you read it with a ref when needed.

### Examples

```jsx
// controlled example
const [name, setName] = useState("");
<input value={name} onChange={e => setName(e.target.value)} />

//uncontrolled example
const inputRef = useRef();
<input ref={inputRef} defaultValue="John" />
// later: inputRef.current.value

````

## when to use what

- Controlled for validation, instant feedback, and syncing state.
- Uncontrolled for quick/simple forms or performance‑heavy inputs.