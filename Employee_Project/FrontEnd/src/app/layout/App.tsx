import React, { useEffect } from 'react';
import { Container } from 'semantic-ui-react';
import NavBar from './NavBar';
import { observer } from 'mobx-react-lite';
import { Route, Switch, useLocation } from 'react-router-dom';
import HomePage from '../../features/home/HomePage';
import { ToastContainer } from 'react-toastify';
import NotFound from '../../features/errors/NotFound';
import ModalContainer from '../common/modals/ModalContainer';
import EmpDashboard from '../../features/employees/dashboard/EmpDashboard';
import EmpDetails from '../../features/employees/details/EmpDetails';
import EmpForm from '../../features/employees/form/EmpForm';
import EmpDelete from '../../features/employees/details/EmpDelete';
import LoadingComponent from './LoadingComponent';
import { useStore } from '../stores/store';
import LoginForm from '../../features/users/LoginForm';

function App() {
  const location = useLocation();
  const {commonStore, userStore} = useStore();

  useEffect(() => {
    if (commonStore.token) {
      userStore.getUser().finally(() => commonStore.setAppLoaded());
    } else {
      commonStore.setAppLoaded();
    }
  }, [commonStore, userStore])

  if (!commonStore.appLoaded) return <LoadingComponent content='Loading app...' />
 
  return (
    <>
      <ToastContainer position='bottom-right' hideProgressBar />
      <ModalContainer />
      <Route exact path='/' component={HomePage} />
      <Route
        path={'/(.+)'}
        render={() => (
          <>
            <NavBar />
            <Container style={{ marginTop: '7em' }}>
              <Switch>
                <Route exact path='/employee' component={EmpDashboard} />
                <Route path='/employee/:id' component={EmpDetails} />
                <Route key={location.key} path={['/createEmployee', '/manage/:id']} component={EmpForm} />
                <Route path='/empdel/:id' component={EmpDelete} />
                <Route path='/login' component={LoginForm} />
                <Route component={NotFound} />
              </Switch>
            </Container>
          </>
        )}
      />
    </>
  );
}

export default observer(App);
