# Designpatterns in pyhton

- Singleton
This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.

- Observer
In this pattern, objects are represented as observers that wait for an event to trigger. An observer attaches to the subject once the specified event occurs. As the event occurs, the subject tells the observers that it has occurred.

- Factory
 In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface.

 - Command
Command Pattern adds a level of abstraction between actions and includes an object, which invokes these actions. 
In this design pattern, client creates a command object that includes a list of commands to be executed. The command object created implements a specific interface.

- Strategy
The strategy pattern is a type of behavioral pattern. The main goal of strategy pattern is to enable client to choose from different algorithms or procedures to complete the specified task. Different algorithms can be swapped in and out without any complications for the mentioned task.
This pattern can be used to improve flexibility when external resources are accessed.

- Builder
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object from its representation so that the same construction process can create different representations.” It allows you to construct complex objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.

- Adapter
Adapter method is a Structural Design Pattern which helps us in making the incompatible objects adaptable to each other. 


- Bridge ???
The bridge method is a Structural Design Pattern that allows us to separate the Implementation Specific Abstractions and Implementation Independent Abstractions from each other and can be developed considering as single entities.
The bridge Method is always considered as one of the best methods to organize the class hierarchy.

- Decorator
Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors. 

- Command
Command Method is Behavioral Design Pattern that encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and the queuing or logging of requests. Parameterizing other objects with different requests in our analogy means that the button used to turn on the lights can later be used to turn on stereo or maybe open the garage door. It helps in promoting the “invocation of a method on an object” to full object status. Basically, it encapsulates all the information needed to perform an action or trigger an event.

- visitor
Visitor Method is a Behavioral Design Pattern which allows us to separate the algorithm from an object structure on which it operates. It helps us to add new features to an existing class hierarchy dynamically without changing it. All the behavioral patterns proved as the best methods to handle the communication between the objects. Similarly, it is used when we have to perform an operation on a group of similar kinds of objects.
