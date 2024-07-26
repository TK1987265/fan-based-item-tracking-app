import React, { useEffect, useState } from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

const LocationItemSchema = Yup.object().shape({
  location_id: Yup.number().required('Required'),
  item_id: Yup.number().required('Required'),
  obtained: Yup.boolean().required('Required'),
});

const LocationItems = () => {
  const [locationItems, setLocationItems] = useState([]);
  const [locations, setLocations] = useState([]);
  const [items, setItems] = useState([]);
  const [editItem, setEditItem] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/locationitems')
      .then(response => response.json())
      .then(data => setLocationItems(data))
      .catch(error => console.error('Error fetching location items:', error));

    fetch('http://localhost:5000/locations')
      .then(response => response.json())
      .then(data => setLocations(data))
      .catch(error => console.error('Error fetching locations:', error));

    fetch('http://localhost:5000/items')
      .then(response => response.json())
      .then(data => setItems(data))
      .catch(error => console.error('Error fetching items:', error));
  }, []);

  const addLocationItem = (values, { resetForm }) => {
    fetch('http://localhost:5000/locationitems', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then(response => response.json())
      .then(data => {
        setLocationItems([...locationItems, data]);
        resetForm();
      })
      .catch(error => console.error('Error adding location item:', error));
  };

  const updateLocationItem = (values, { resetForm }) => {
    fetch(`http://localhost:5000/locationitems/${editItem.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then(response => response.json())
      .then(data => {
        setLocationItems(locationItems.map(item => (item.id === data.id ? data : item)));
        setEditItem(null);
        resetForm();
      })
      .catch(error => console.error('Error updating location item:', error));
  };

  const deleteLocationItem = (id) => {
    fetch(`http://localhost:5000/locationitems/${id}`, {
      method: 'DELETE',
    })
      .then(response => response.json())
      .then(() => {
        setLocationItems(locationItems.filter(item => item.id !== id));
      })
      .catch(error => console.error('Error deleting location item:', error));
  };

  const getLocationNameById = (id) => {
    const location = locations.find(location => location.id === id);
    return location ? location.name : 'Unnamed location';
  };

  const getItemNameById = (id) => {
    const item = items.find(item => item.id === id);
    return item ? item.name : 'Unnamed item';
  };

  return (
    <div>
      <h2>Location Items</h2>
      <Formik
        initialValues={{
          location_id: editItem ? editItem.location_id : '',
          item_id: editItem ? editItem.item_id : '',
          obtained: editItem ? editItem.obtained : false
        }}
        enableReinitialize
        validationSchema={LocationItemSchema}
        onSubmit={editItem ? updateLocationItem : addLocationItem}
      >
        {({ errors, touched }) => (
          <Form>
            <div>
              <label htmlFor="location_id">Location</label>
              <Field as="select" name="location_id">
                <option value="">Select Location</option>
                {locations.map(location => (
                  <option key={location.id} value={location.id}>{location.name}</option>
                ))}
              </Field>
              {errors.location_id && touched.location_id ? <div>{errors.location_id}</div> : null}
            </div>
            <br/>
            <div>
              <label htmlFor="item_id">Item</label>
              <Field as="select" name="item_id">
                <option value="">Select Item</option>
                {items.map(item => (
                  <option key={item.id} value={item.id}>{item.name}</option>
                ))}
              </Field>
              {errors.item_id && touched.item_id ? <div>{errors.item_id}</div> : null}
            </div>
            <br/>
            <div>
              <label>
                <Field type="checkbox" name="obtained" />
                Obtained
              </label>
              {errors.obtained && touched.obtained ? <div>{errors.obtained}</div> : null}
            </div>
            <br/>
            <button type="submit">{editItem ? 'Update' : 'Add'} Location Item</button>
            {editItem && <button type="button" onClick={() => setEditItem(null)}>Cancel</button>}
          </Form>
        )}
      </Formik>
      <ul className="loc-items">
        {locationItems.map(locationItem => (
          <li key={locationItem.id}>
            {getLocationNameById(locationItem.location_id)} - {getItemNameById(locationItem.item_id)} - {locationItem.obtained ? 'Obtained' : 'Not Obtained'}
            &nbsp;&nbsp;<button onClick={() => setEditItem(locationItem)}>Edit</button>
            <button onClick={() => deleteLocationItem(locationItem.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LocationItems;
