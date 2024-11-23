## AWS API
![image_0_Image9.jpg.png](./img/image_0_Image9.jpg.png)

## User
-	When you sign-up first time, its creates root user
-	never use this root user

STEP 1 : create new IAM user using root user
STEP 2 : Enable console access for that user to access AWS console & set the password
![image_0_Image10.jpg.png](./img/image_0_Image10.jpg.png)

STEP 3 : Attach the policy as per requirement
![image_1_Image14.jpg.png](./img/image_1_Image14.jpg.png)

STEP 4 : Create access key to access user through CLI
![image_1_Image15.png.png](./img/image_1_Image15.png.png)

## AWS CLI
![image_1_Image16.png.png](./img/image_1_Image16.png.png)
![image_2_Image19.jpg.png](./img/image_2_Image19.jpg.png)
![image_2_Image20.jpg.png](./img/image_2_Image20.jpg.png)
![image_2_Image21.jpg.png](./img/image_2_Image21.jpg.png)

Install AWS CLI 

Following command will show credentials of Root account 
![image_3_Image24.jpg.png](./img/image_3_Image24.jpg.png)

There credentials are stored in config & credentials file
![image_3_Image25.jpg.png](./img/image_3_Image25.jpg.png)
![image_3_Image26.png.png](./img/image_3_Image26.png.png)
![image_4_Image29.jpg.png](./img/image_4_Image29.jpg.png)


Create new user on AWS console and create its keys

Add the keys in both the files as follows

![image_4_Image30.jpg.png](./img/image_4_Image30.jpg.png)
![image_4_Image31.png.png](./img/image_4_Image31.png.png)

By default commands will be executed for root user 
![image_4_Image32.jpg.png](./img/image_4_Image32.jpg.png)

Execute command for specific user
![image_4_Image33.jpg.png](./img/image_4_Image33.jpg.png)

## IAM (Identity & Access Management) 
![image_5_Image45.jpg.png](./img/image_5_Image45.jpg.png)

Policy : set of permissions (what is allowed & not allowed)

Role : We can apply the policy to the user, resources, groups or a Role. (e.g., apply all developer related policy to a role name role_dev. Then assign this role to a user that is a developer
Role vs Group
- Role: Use roles when you need to grant temporary or specific permissions to an AWS resource or service. Policies attached to roles determine what actions can be performed by entities that assume the role.
- Group: Use groups to manage permissions for a set of IAM users collectively. Policies attached to groups dictate what permissions users in that group receive.
In essence, roles are more dynamic and are used to grant permissions to entities that need them temporarily or conditionally, while groups are static and used for managing permissions among a set of users.


![image_6_Image48.jpg.png](./img/image_6_Image48.jpg.png)
![image_7_Image51.jpg.png](./img/image_7_Image51.jpg.png)
![image_7_Image52.jpg.png](./img/image_7_Image52.jpg.png)
![image_8_Image55.jpg.png](./img/image_8_Image55.jpg.png)
![image_8_Image56.jpg.png](./img/image_8_Image56.jpg.png)
![image_8_Image57.jpg.png](./img/image_8_Image57.jpg.png)
![image_9_Image60.jpg.png](./img/image_9_Image60.jpg.png)
![image_9_Image61.jpg.png](./img/image_9_Image61.jpg.png)
![image_10_Image64.jpg.png](./img/image_10_Image64.jpg.png)
![image_10_Image65.jpg.png](./img/image_10_Image65.jpg.png)
## IAM Best Practice 
![image_10_Image66.jpg.png](./img/image_10_Image66.jpg.png)

### Service control policy
![image_11_Image69.jpg.png](./img/image_11_Image69.jpg.png)

## Roles

2 ways of assigning policies

Directly to the user/resources OR through Roles

![image_12_Image72.jpg.png](./img/image_12_Image72.jpg.png)
![image_12_Image73.jpg.png](./img/image_12_Image73.jpg.png)

How to create and assign roles
![image_13_Image76.jpg.png](./img/image_13_Image76.jpg.png)

Create a role
![image_13_Image77.png.png](./img/image_13_Image77.png.png)

Attach policy to role
![image_14_Image80.png.png](./img/image_14_Image80.png.png)
![image_14_Image81.png.png](./img/image_14_Image81.png.png)

Use this link to use the role
![image_14_Image82.png.png](./img/image_14_Image82.png.png)

But make sure only the user who assumes the role can access it or else you will get error
![image_15_Image85.png.png](./img/image_15_Image85.png.png)

assign/assume the to user1
![image_15_Image86.png.png](./img/image_15_Image86.png.png)
![image_15_Image88.png.png](./img/image_15_Image88.png.png)
![image_16_Image91.png.png](./img/image_16_Image91.png.png)

User permissions & Policies
![image_17_Image94.jpg.png](./img/image_17_Image94.jpg.png)
![image_17_Image95.jpg.png](./img/image_17_Image95.jpg.png)

Resource Based Policies 
![image_18_Image98.jpg.png](./img/image_18_Image98.jpg.png)
![image_18_Image99.jpg.png](./img/image_18_Image99.jpg.png)

EC2 (Elastic Cloud Compute)
![image_19_Image102.jpg.png](./img/image_19_Image102.jpg.png)
![image_19_Image103.jpg.png](./img/image_19_Image103.jpg.png)
![image_20_Image106.jpg.png](./img/image_20_Image106.jpg.png)

Key Pair
![image_20_Image107.png.png](./img/image_20_Image107.png.png)
![image_20_Image108.jpg.png](./img/image_20_Image108.jpg.png)
![image_21_Image111.png.png](./img/image_21_Image111.png.png)

Private key downloaded automatically
![image_21_Image112.png.png](./img/image_21_Image112.png.png)
![image_22_Image115.jpg.png](./img/image_22_Image115.jpg.png)
![image_22_Image116.png.png](./img/image_22_Image116.png.png)
![image_22_Image117.jpg.png](./img/image_22_Image117.jpg.png)
![image_23_Image120.jpg.png](./img/image_23_Image120.jpg.png)

User Data

1 : For Ubuntu 
![image_23_Image121.jpg.png](./img/image_23_Image121.jpg.png)

Cmd to check logs if any error occurs 
![image_23_Image122.jpg.png](./img/image_23_Image122.jpg.png)

2 : For amazon linux
![image_24_Image125.png.png](./img/image_24_Image125.png.png)


Security Groups 
Used to set rules as to which port or IP is allowed


V/S Firewall 

Firewall blocks external traffic, where as security groups blocks internal VPC traffic as well
![image_25_Image128.jpg.png](./img/image_25_Image128.jpg.png)

Inbound (incoming traffic)

set rules on incoming traffic 
![image_26_Image131.jpg.png](./img/image_26_Image131.jpg.png)

Outbound (outgoing traffic)

set rules on outgoing traffic 
![image_26_Image132.jpg.png](./img/image_26_Image132.jpg.png)
![image_26_Image133.png.png](./img/image_26_Image133.png.png)

E.g., Accessing internet from VM
![image_27_Image136.jpg.png](./img/image_27_Image136.jpg.png)

EBS (Elastic Block Storage)

This storage can be used to store OS

Should be in the same AZ

![image_28_Image139.jpg.png](./img/image_28_Image139.jpg.png)

4 Types of EBS 
![image_28_Image140.jpg.png](./img/image_28_Image140.jpg.png)

8 GB volume attached while creating EC2 
![image_29_Image143.jpg.png](./img/image_29_Image143.jpg.png)

Attach Additional Volume

create a volume and attach it from the console
make sure you create the volume in the same AZ

![image_29_Image144.jpg.png](./img/image_29_Image144.jpg.png)
![image_30_Image152.jpg.png](./img/image_30_Image152.jpg.png)

check the disk partition
![image_30_Image153.jpg.png](./img/image_30_Image153.jpg.png)
![image_30_Image154.jpg.png](./img/image_30_Image154.jpg.png)

check the file system of the volume
![image_30_Image155.jpg.png](./img/image_30_Image155.jpg.png)

If it shows “data” that means there is no file system for our volume	


create xfs file system
![image_31_Image158.jpg.png](./img/image_31_Image158.jpg.png)
![image_31_Image159.jpg.png](./img/image_31_Image159.jpg.png)

mount the volume
![image_31_Image160.png.png](./img/image_31_Image160.png.png)

 verify 
![image_31_Image161.jpg.png](./img/image_31_Image161.jpg.png)

S3 (Simple Storage Service)
![image_32_Image164.jpg.png](./img/image_32_Image164.jpg.png)
![image_32_Image165.jpg.png](./img/image_32_Image165.jpg.png)

Static website hosting
![image_33_Image168.jpg.png](./img/image_33_Image168.jpg.png)

## EFS 
## EQS


Lambda

lambda is basically a server less servce

![image_34_Image171.jpg.png](./img/image_34_Image171.jpg.png)

Advantages over EC2
![image_34_Image172.png.png](./img/image_34_Image172.png.png)

Create a Lambda
![image_35_Image177.png.png](./img/image_35_Image177.png.png)

write your code inside lambda_handler() function
![image_35_Image178.jpg.png](./img/image_35_Image178.jpg.png)

deploy the code
![image_36_Image178.jpg.png](./img/image_36_Image178.jpg.png)

 click on Test write a test case/event. you can have customized test events with its own set of inputs
![image_36_Image181.png.png](./img/image_36_Image181.png.png)
![image_37_Image184.jpg.png](./img/image_37_Image184.jpg.png)

2 ways to upload lambda zip
## 1 : directly upload the zip
## 2 : Upload the zip to S3 and enter its ARN 


Create lambda URL
![image_37_Image185.jpg.png](./img/image_37_Image185.jpg.png)

1 : Public URL
![image_38_Image188.jpg.png](./img/image_38_Image188.jpg.png)
![image_38_Image189.jpg.png](./img/image_38_Image189.jpg.png)

2 : Private URL
![image_38_Image190.jpg.png](./img/image_38_Image190.jpg.png)
![image_39_Image193.jpg.png](./img/image_39_Image193.jpg.png)

Environment Variable 
![image_39_Image194.png.png](./img/image_39_Image194.png.png)
![image_39_Image195.png.png](./img/image_39_Image195.png.png)
![image_40_Image198.jpg.png](./img/image_40_Image198.jpg.png)

## Lambda Layers

Lambda layers are nothing but libraries. Instead of writing redundant code, write a lambda layer and use to in multiple places 

![image_40_Image199.jpg.png](./img/image_40_Image199.jpg.png)

## Containers
![image_41_Image202.png.png](./img/image_41_Image202.png.png)

## Monolithic vs Microservices
![image_41_Image203.jpg.png](./img/image_41_Image203.jpg.png)