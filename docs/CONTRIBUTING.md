# Contributing to CuraAI

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Submit a pull request

## Development Setup

See [SETUP.md](./SETUP.md) for detailed setup instructions.

## Code Style

### Python (Backend)

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused

```python
def get_user_health_records(user_id):
    """Get health records for a specific user.
    
    Args:
        user_id (int): User ID
        
    Returns:
        list: List of health records
    """
    records = HealthRecord.query.filter_by(user_id=user_id).all()
    return records
```

### JavaScript/React (Frontend)

- Use ES6+ syntax
- Use functional components
- Add comments for complex logic
- Use meaningful component and variable names

```javascript
// Good
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    // Fetch user data
  }, [userId]);
  
  return <div>{/* JSX */}</div>;
};
```

## Commit Messages

- Use clear, descriptive messages
- Use imperative mood ("Add feature" not "Added feature")
- Keep messages concise

```
Add health tracking feature
Fix bug in appointment booking
Update API documentation
```

## Pull Request Process

1. Update README.md with any new features
2. Update documentation as needed
3. Ensure tests pass
4. Request review from maintainers
5. Address feedback

## Reporting Issues

When reporting bugs, include:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots if applicable

## Feature Requests

When proposing features:
- Explain the use case
- Describe expected behavior
- Suggest implementation approach

## Code Review Guidelines

- Be respectful and constructive
- Focus on code, not the person
- Suggest improvements, not demands
- Acknowledge good work

## Questions?

Open an issue or contact the maintainers.
