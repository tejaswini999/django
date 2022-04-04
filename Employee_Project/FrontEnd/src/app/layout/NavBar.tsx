import { observer } from "mobx-react-lite";
import React from "react";
import { Link, NavLink } from 'react-router-dom';
import { Button, Container, Menu, Image, Dropdown } from 'semantic-ui-react';
import { useStore } from "../stores/store";

export default observer(function NavBar() {
  const { userStore: { user, logout } } = useStore();

  return (
    <Menu inverted fixed="top">
      <Container>
        <Menu.Item as={NavLink} exact to="/" header>
          <img
            src="/assets/logo.png"
            alt="logo"
            style={{ marginRight: "10px" }}
          />
          Employees
        </Menu.Item>
        <Menu.Item as={NavLink} to="/employee" name="Employees" />
        <Menu.Item>
          <Button
            as={NavLink}
            to="/createEmployee"
            positive
            content="Create Employee"
          />
        </Menu.Item>
        <Menu.Item position='right'>
          <Dropdown pointing='top left' text={user?.displayName}>
            <Dropdown.Menu>
               <Dropdown.Item onClick={logout} text='Logout' icon='power' />
             </Dropdown.Menu>
          </Dropdown>
          </Menu.Item>
      </Container>
    </Menu>
  );
});
