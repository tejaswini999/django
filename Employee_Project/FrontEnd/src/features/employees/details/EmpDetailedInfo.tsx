import { observer } from 'mobx-react-lite';
import { Segment, Grid, Icon } from 'semantic-ui-react'
import { Employee } from "../../../app/models/employee";
import {format} from 'date-fns';

interface Props {
    employee: Employee
}

export default observer(function EmployeeDetailedInfo({ employee }: Props) {
   function convertDate(str:any) {
        var date = new Date(str),
          mnth = ("0" + (date.getMonth() + 1)).slice(-2),
          day = ("0" + date.getDate()).slice(-2);
        return [date.getFullYear(), mnth, day].join("-");
      }
  employee.empDOJ=new Date(convertDate(employee.empDOJ))
    return (
        <Segment.Group>
            <Segment attached='top'>
                <Grid>
                    <Grid.Column width={1}>
                        <Icon size='large' color='teal' name='info' />
                    </Grid.Column>
                    <Grid.Column width={15}>
                        <p>{employee.empDescription}</p>
                    </Grid.Column>
                </Grid>
            </Segment>
            <Segment attached>
                <Grid verticalAlign='middle'>
                    <Grid.Column width={1}>
                        <Icon name='calendar' size='large' color='teal' />
                    </Grid.Column>
                    <Grid.Column width={15}>
                        <span>
                            {convertDate(employee.empDOJ)}
                        </span>
                    </Grid.Column>
                </Grid>
            </Segment>
            <Segment attached>
                <Grid verticalAlign='middle'>
                    <Grid.Column width={1}>
                        <Icon name='marker' size='large' color='teal' />
                    </Grid.Column>
                    <Grid.Column width={11}>
                        <span>{employee.empOfficeVenue}, {employee.empCity}</span>
                    </Grid.Column>
                </Grid>
            </Segment>
        </Segment.Group>
    )
})