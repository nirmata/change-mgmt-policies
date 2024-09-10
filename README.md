This is a demo repository to scan CloudFormation templates. The scanned results can be viewed via the [Nirmata Policy Manager (NPM)]([url](https://nirmata.com/policy-manager/)).

The GitHub Action converts the CDK file into a CloudFormation template using the `cdk synth` command. The policies are applied on the generated JSON file. The results are then published to NPM.

![image](https://github.com/user-attachments/assets/2be97d3a-3833-4a42-971c-062b3e992108)

