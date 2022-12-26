'use strict'
module.exports = {
	up: (queryInterface, Sequelize) => {
		return queryInterface.createTable("lead", {
			id: {
				allowNull: false,
				primaryKey: true,
				type: Sequelize.UUID,
				defaultValue: Sequelize.UUIDV4
			},
			createdAt: {
				allowNull: false,
				type: Sequelize.DATE
			},
			updatedAt: {
				alowNull: false,
				type: Sequelize.DATE
			},
			email: {
				allowNull: false,
				type: Sequelize.STRING
			}
		})
	},
	down: (queryInterface, Sequelize) => {
		return queryInterface.dropTable("lead");
	}
}