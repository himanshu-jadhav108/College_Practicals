## Trial ER Diagram

```mermaid
erDiagram
DEPARTMENTS ||--o{ STUDENTS : has

DEPARTMENTS {
  int id
  string name
}

STUDENTS {
  int id
  string name
  string email
  int dept_id
}
```

### By Himanshu Jadhav