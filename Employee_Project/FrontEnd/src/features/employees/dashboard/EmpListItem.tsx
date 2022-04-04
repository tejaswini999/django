import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Icon, Item, Segment } from 'semantic-ui-react';
import { Employee } from '../../../app/models/employee';
import {format} from 'date-fns';

interface Props {
    employee: Employee
}

export default function EmployeeListItem({ employee }: Props) {
    return (
        <Segment.Group>
            <Segment>
                <Item.Group>
                    <Item>
                        <Item.Image size='tiny' circular src='/assets/user.png' />
                        <Item.Content>
                            <Item.Header as={Link} to={`/employee/${employee.empID}`}>
                                {employee.empName}
                            </Item.Header>
                            <Item.Description> {employee.empDescription}</Item.Description>
                        </Item.Content>
                    </Item>
                </Item.Group>
            </Segment>
            <Segment>
                <span>
                    <Icon name='clock' /> {format(employee.empDOJ!, 'dd MMM yyyy ')}
                    <Icon name='marker' /> {employee.empOfficeVenue}
                </span>
            </Segment>
            <Segment clearing>
                <span>{employee.empDescription}</span>
                <Button 
                    as={Link}
                    to={`/employee/${employee.empID}`}
                    color='teal'
                    floated='right'
                    content='View'
                />
                <Button 
                    as={Link}
                    to={`/empdel/${employee.empID}`}
                    color='teal'
                    floated='right'
                    content='Delete'
                />
            </Segment>
        </Segment.Group>
    )
}