import { observer } from 'mobx-react-lite';
import React, { useEffect } from 'react';
import { Grid, Header, Icon, Segment} from 'semantic-ui-react';
import LoadingComponent from '../../../app/layout/LoadingComponent';
import { useStore } from '../../../app/stores/store';
import EmpList from './EmpList';

export default observer(function ActivityDashboard() {
    const {empStore, userStore, commonStore} = useStore();
    const {loadEmployees, employeeRegistry} = empStore;

    useEffect(() => {
        if (employeeRegistry.size <= 1) loadEmployees();
    }, [employeeRegistry.size, loadEmployees, userStore, commonStore], )
  
    if (empStore.loadingInitial) return <LoadingComponent content='Loading employees...' />

    return (
        <>
             {employeeRegistry.size<1 ?
        (
            <>
             <Segment placeholder>
             <Header icon>
                 <Icon name='search' />
                    No Records Found for Employee !
             </Header>            
         </Segment>
         </>
        ):
        (
            <>
        <Grid>
        <Grid.Column width='10'>
            <EmpList />
        </Grid.Column>
        <Grid.Column width='6'>
            </Grid.Column>
        </Grid>
        </>
)}
          </>  
    )
})