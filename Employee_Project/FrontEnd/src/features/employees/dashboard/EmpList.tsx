import { observer } from 'mobx-react-lite';
import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';
import { useStore } from '../../../app/stores/store';
import EmpListItem from './EmpListItem';

export default observer(function EmployeeList() {
    const { empStore } = useStore();
    const { groupedEmployee } = empStore;
    return (
        <>
            {groupedEmployee.map(([group, employees]) => (
                <Fragment key={group}>
                    <Header sub color='teal'>
                        {group}
                    </Header>
                    {employees.map(employee => (
                        <EmpListItem key={employee.empID} employee={employee} />
                    ))}
                </Fragment>
            ))}
        </>

    )
})