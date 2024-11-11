import { useEffect, useState} from "react"
import {getAllTasks} from '../api/tasks.api.js'
import { TaskCard } from "./TaskCard.jsx"

export function TaskList() {

    const [tasks, setTasks] = useState([])

    useEffect(() => {
        async function loadTasks(){
            const res = await getAllTasks()
            setTasks(res.data)
        }
        loadTasks();
    }, [])

  return <div>
    {tasks.map(task => (
    < TaskCard key = { task.id } task={task}/>
  ))}
  </div>;
}