import { toJS } from 'mobx';
import { observer } from 'mobx-react-lite';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Grid } from 'semantic-ui-react';
import LoadingComponent from '../../../app/layout/LoadingComponent';
import { Employee } from '../../../app/models/employee';
import { useStore } from '../../../app/stores/store';
import EmpDetailedHeader from './EmpDetailedHeader';
import EmpDetailedInfo from './EmpDetailedInfo';

export default observer(function EmployeeDetails() {
    const {empStore} = useStore();
    const {selectedEmployee:employee,loademployee,loadingInitial} = empStore;
    const {id} = useParams<{id: string}>();
 
    useEffect(() => {
        if (id)
           loademployee(Number(id))
    }, [id, loademployee]);

    if (loadingInitial || !employee) return <LoadingComponent />;
    return (
        <Grid>
            <Grid.Column width={10}>
               <EmpDetailedHeader employee={toJS(employee)} /> 
                 <EmpDetailedInfo employee={toJS(employee)} /> 
            </Grid.Column>
            <Grid.Column width={6}>
            </Grid.Column>
        </Grid>
    )
})