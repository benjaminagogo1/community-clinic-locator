const mongoose = require('mongoose');
const clinicSchema = new mongoose.Schema({
    name: String,
    address: String,
    services: [String],
    location: {
        lat: Number,
        lng: Number
    }
});
module.exports = mongoose.model('Clinic', clinicSchema);
