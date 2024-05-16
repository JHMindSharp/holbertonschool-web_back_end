const CarSymbol = Symbol('Car');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return Object.assign(Object.create(Object.getPrototypeOf(this)), {
      [CarSymbol]: true,
    });
  }
}
