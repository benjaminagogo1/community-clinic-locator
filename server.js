const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const cors = require('cors');

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

const authRoutes = require('./routes/authRoutes');
const clinicRoutes = require('./routes/clinicRoutes');

app.use('/api/auth', authRoutes);
app.use('/api/clinics', clinicRoutes);

mongoose.connect(process.env.MONGO_URI)
    .then(() => {
        app.listen(process.env.PORT || 5000, () => console.log('Server running'));
    })
    .catch(err => console.log(err));
