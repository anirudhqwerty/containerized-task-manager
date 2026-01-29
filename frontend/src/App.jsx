import { useEffect, useState } from "react";

const API_URL = "/api";

function App() {
  const [title, setTitle] = useState("");
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    const res = await fetch(`${API_URL}/tasks`);
    const data = await res.json();
    setTasks(data);
  };

  const createTask = async () => {
    if (!title) return;

    await fetch(`${API_URL}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });

    setTitle("");
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
    const interval = setInterval(fetchTasks, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h2>Task Manager</h2>

      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Task title"
      />
      <button onClick={createTask}>Create Task</button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.title} — <b>{task.status}</b>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
