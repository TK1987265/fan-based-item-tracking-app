import React, { useEffect, useState } from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

const LocationSchema = Yup.object().shape({
  name: Yup.string().required('Required'),
});

const Locations = () => {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/locations')
      .then(response => response.json())
      .then(data => setLocations(data));
  }, []);

  const addLocation = (values, { resetForm }) => {
    fetch('http://localhost:5000/locations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then(response => response.json())
      .then(data => {
        setLocations([...locations, data]);
        resetForm();
      });
  };

  return (
    <div>
      <h2>Locations</h2>
      <Formik
        initialValues={{ name: '' }}
        validationSchema={LocationSchema}
        onSubmit={addLocation}
      >
        {({ errors, touched }) => (
          <Form>
            <Field name="name" />
            {errors.name && touched.name ? <div>{errors.name}</div> : null}
            <button type="submit">Add Location</button>
          </Form>
        )}
      </Formik>
      <ul>
        {locations.map(location => (
          <li key={location.id}>{location.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Locations;
