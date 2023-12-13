export default function clientToken() {

  const login = (id, name) => {
        sessionStorage.setItem('userId', JSON.stringify(id));
        sessionStorage.setItem('userName', JSON.stringify(name));
  }

  const logout = () => {
    sessionStorage.removeItem('userId')
    sessionStorage.removeItem('userName')
  }

  const userName = () => {
    const tokenString = sessionStorage.getItem('userName');
    if (tokenString) {
        const userData = JSON.parse(tokenString);
        return userData;
  }
  return null;
}

const userId = () => {
    const tokenString = sessionStorage.getItem('userId');
    if (tokenString) {
        const userData = JSON.parse(tokenString);
        return userData;
  }
  return null;
}

  return {login, logout, userName, userId}
}