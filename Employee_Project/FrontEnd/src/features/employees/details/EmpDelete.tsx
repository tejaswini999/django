import { observer } from 'mobx-react-lite';
import { useEffect } from 'react';
import {  useHistory, useParams } from 'react-router-dom';
import { toast } from 'react-toastify';
import LoadingComponent from '../../../app/layout/LoadingComponent';
import { useStore } from '../../../app/stores/store';


export default observer(function EmployeeDetails() {
    const history = useHistory();
    const {empStore} = useStore();
    const {deleteemployee,employeeRegistry} = empStore;
    const {id} = useParams<{id: string}>();

    useEffect(() => {
        (async () => {
        if (id)
        {
           await deleteemployee(Number(id));
        } 
        else{
            toast.error("No Item Selected")
         }
         window.location.href = "/employee"
        })()       
    }, [id, deleteemployee]);

    return (
        <>
        <LoadingComponent content='Deleting Employee...' />     
       </>
    )
})


