export default function employeeToken() {

    const login = (id, name, type) => {
          sessionStorage.setItem('userId', JSON.stringify(id));
          sessionStorage.setItem('userName', JSON.stringify(name));
          sessionStorage.setItem('userType', JSON.stringify(type));
    }

    const logout = () => {
      sessionStorage.removeItem('userId')
      sessionStorage.removeItem('userName')
      sessionStorage.removeItem('userType')
    }

  const userId = () => {
      const tokenString = sessionStorage.getItem('userId');
      if (tokenString) {
          const userData = JSON.parse(tokenString);
          return userData;
    }
    return null;
  }

  const userName = () => {
    const tokenString = sessionStorage.getItem('userName');
    if (tokenString) {
        const userData = JSON.parse(tokenString);
        return userData;
  }
  return null;
}

  const userType = () => {
    const tokenString = sessionStorage.getItem('userType');
    if (tokenString) {
      const userData = JSON.parse(tokenString);
      return userData;
    }
    return null;
  }

    return {login, logout, userName, userId, userType}
  }