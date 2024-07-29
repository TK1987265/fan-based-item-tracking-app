import React, { useEffect, useState } from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

const ItemSchema = Yup.object().shape({
  name: Yup.string().required('Required'),
  cost: Yup.number().required('Required').positive('Cost must be a positive number'),
});

const Items = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/items')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  const addItem = (values, { resetForm }) => {
    fetch('http://localhost:5000/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then(response => response.json())
      .then(data => {
        setItems([...items, data]);
        resetForm();
      });
  };

   return (
    <div>
      <h2>Items</h2>
      <Formik
        initialValues={{ name: '', cost: '' }}
        validationSchema={ItemSchema}
        onSubmit={addItem}
      >
        {({ errors, touched }) => (
          <Form>
            <div>
              <label>Name:</label>
              <Field name="name" />
              {errors.name && touched.name ? <div>{errors.name}</div> : null}
            </div>
            <div>
              <label>Cost:</label>
              <Field name="cost" type="number" />
              {errors.cost && touched.cost ? <div>{errors.cost}</div> : null}
            </div>
            <button type="submit">Add Item</button>
          </Form>
        )}
      </Formik>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} - ${item.cost}
          
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Items;
