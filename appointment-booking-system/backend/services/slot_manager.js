/**
 * Smart Slot Manager
 * Unique Feature: Efficient Overlap Detection using Time Intervals
 */

const moment = require('moment'); // Assumed dependency

class SlotManager {
    constructor() {
        this.bookings = []; // Mock database
    }

    /**
     * Checks if a requested slot overlaps with existing bookings.
     * @param {string} startTime - ISO String
     * @param {string} endTime - ISO String
     * @returns {boolean} - True if available, False if conflict
     */
    isSlotAvailable(startTime, endTime) {
        const start = new Date(startTime).getTime();
        const end = new Date(endTime).getTime();

        return !this.bookings.some(booking => {
            const bStart = new Date(booking.startTime).getTime();
            const bEnd = new Date(booking.endTime).getTime();

            // Overlap logic: (StartA < EndB) and (EndA > StartB)
            return (start < bEnd && end > bStart);
        });
    }

    bookSlot(user, startTime, endTime) {
        if (this.isSlotAvailable(startTime, endTime)) {
            this.bookings.push({ user, startTime, endTime });
            return { success: true, message: "Booking Confirmed! ✅" };
        } else {
            return { success: false, message: "Conflict Detected! ❌ Slot already taken." };
        }
    }
}

module.exports = new SlotManager();
