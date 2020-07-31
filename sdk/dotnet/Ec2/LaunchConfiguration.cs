// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Provides a resource to create a new launch configuration, used for autoscaling groups.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var ubuntu = Output.Create(Aws.GetAmi.InvokeAsync(new Aws.GetAmiArgs
    ///         {
    ///             MostRecent = true,
    ///             Filters = 
    ///             {
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "name",
    ///                     Values = 
    ///                     {
    ///                         "ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*",
    ///                     },
    ///                 },
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "virtualization-type",
    ///                     Values = 
    ///                     {
    ///                         "hvm",
    ///                     },
    ///                 },
    ///             },
    ///             Owners = 
    ///             {
    ///                 "099720109477",
    ///             },
    ///         }));
    ///         var asConf = new Aws.Ec2.LaunchConfiguration("asConf", new Aws.Ec2.LaunchConfigurationArgs
    ///         {
    ///             ImageId = ubuntu.Apply(ubuntu =&gt; ubuntu.Id),
    ///             InstanceType = "t2.micro",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Using with AutoScaling Groups
    /// 
    /// Launch Configurations cannot be updated after creation with the Amazon
    /// Web Service API. In order to update a Launch Configuration, this provider will
    /// destroy the existing resource and create a replacement. In order to effectively
    /// use a Launch Configuration resource with an [AutoScaling Group resource](https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html),
    /// it's recommended to specify `create_before_destroy` in a [lifecycle](https://www.terraform.io/docs/configuration/resources.html#lifecycle) block.
    /// Either omit the Launch Configuration `name` attribute, or specify a partial name
    /// with `name_prefix`.  Example:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var ubuntu = Output.Create(Aws.GetAmi.InvokeAsync(new Aws.GetAmiArgs
    ///         {
    ///             MostRecent = true,
    ///             Filters = 
    ///             {
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "name",
    ///                     Values = 
    ///                     {
    ///                         "ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*",
    ///                     },
    ///                 },
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "virtualization-type",
    ///                     Values = 
    ///                     {
    ///                         "hvm",
    ///                     },
    ///                 },
    ///             },
    ///             Owners = 
    ///             {
    ///                 "099720109477",
    ///             },
    ///         }));
    ///         var asConf = new Aws.Ec2.LaunchConfiguration("asConf", new Aws.Ec2.LaunchConfigurationArgs
    ///         {
    ///             NamePrefix = "lc-example-",
    ///             ImageId = ubuntu.Apply(ubuntu =&gt; ubuntu.Id),
    ///             InstanceType = "t2.micro",
    ///         });
    ///         var bar = new Aws.AutoScaling.Group("bar", new Aws.AutoScaling.GroupArgs
    ///         {
    ///             LaunchConfiguration = asConf.Name,
    ///             MinSize = 1,
    ///             MaxSize = 2,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// With this setup this provider generates a unique name for your Launch
    /// Configuration and can then update the AutoScaling Group without conflict before
    /// destroying the previous Launch Configuration.
    /// 
    /// ## Using with Spot Instances
    /// 
    /// Launch configurations can set the spot instance pricing to be used for the
    /// Auto Scaling Group to reserve instances. Simply specifying the `spot_price`
    /// parameter will set the price on the Launch Configuration which will attempt to
    /// reserve your instances at this price.  See the [AWS Spot Instance
    /// documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
    /// for more information or how to launch [Spot Instances](https://www.terraform.io/docs/providers/aws/r/spot_instance_request.html) with this provider.
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var ubuntu = Output.Create(Aws.GetAmi.InvokeAsync(new Aws.GetAmiArgs
    ///         {
    ///             MostRecent = true,
    ///             Filters = 
    ///             {
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "name",
    ///                     Values = 
    ///                     {
    ///                         "ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*",
    ///                     },
    ///                 },
    ///                 new Aws.Inputs.GetAmiFilterArgs
    ///                 {
    ///                     Name = "virtualization-type",
    ///                     Values = 
    ///                     {
    ///                         "hvm",
    ///                     },
    ///                 },
    ///             },
    ///             Owners = 
    ///             {
    ///                 "099720109477",
    ///             },
    ///         }));
    ///         var asConf = new Aws.Ec2.LaunchConfiguration("asConf", new Aws.Ec2.LaunchConfigurationArgs
    ///         {
    ///             ImageId = ubuntu.Apply(ubuntu =&gt; ubuntu.Id),
    ///             InstanceType = "m4.large",
    ///             SpotPrice = "0.001",
    ///         });
    ///         var bar = new Aws.AutoScaling.Group("bar", new Aws.AutoScaling.GroupArgs
    ///         {
    ///             LaunchConfiguration = asConf.Name,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Block devices
    /// 
    /// Each of the `*_block_device` attributes controls a portion of the AWS
    /// Launch Configuration's "Block Device Mapping". It's a good idea to familiarize yourself with [AWS's Block Device
    /// Mapping docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html)
    /// to understand the implications of using these attributes.
    /// 
    /// The `root_block_device` mapping supports the following:
    /// 
    /// * `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
    ///   or `"io1"`. (Default: `"standard"`).
    /// * `volume_size` - (Optional) The size of the volume in gigabytes.
    /// * `iops` - (Optional) The amount of provisioned
    ///   [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
    ///   This must be set with a `volume_type` of `"io1"`.
    /// * `delete_on_termination` - (Optional) Whether the volume should be destroyed
    ///   on instance termination (Default: `true`).
    /// * `encrypted` - (Optional) Whether the volume should be encrypted or not. (Default: `false`).
    /// 
    /// Modifying any of the `root_block_device` settings requires resource
    /// replacement.
    /// 
    /// Each `ebs_block_device` supports the following:
    /// 
    /// * `device_name` - (Required) The name of the device to mount.
    /// * `snapshot_id` - (Optional) The Snapshot ID to mount.
    /// * `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
    ///   or `"io1"`. (Default: `"standard"`).
    /// * `volume_size` - (Optional) The size of the volume in gigabytes.
    /// * `iops` - (Optional) The amount of provisioned
    ///   [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
    ///   This must be set with a `volume_type` of `"io1"`.
    /// * `delete_on_termination` - (Optional) Whether the volume should be destroyed
    ///   on instance termination (Default: `true`).
    /// * `encrypted` - (Optional) Whether the volume should be encrypted or not. Do not use this option if you are using `snapshot_id` as the encrypted flag will be determined by the snapshot. (Default: `false`).
    /// 
    /// Modifying any `ebs_block_device` currently requires resource replacement.
    /// 
    /// Each `ephemeral_block_device` supports the following:
    /// 
    /// * `device_name` - The name of the block device to mount on the instance.
    /// * `virtual_name` - The [Instance Store Device
    ///   Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
    ///   (e.g. `"ephemeral0"`)
    /// 
    /// Each AWS Instance type has a different set of Instance Store block devices
    /// available for attachment. AWS [publishes a
    /// list](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes)
    /// of which ephemeral devices are available on each type. The devices are always
    /// identified by the `virtual_name` in the format `"ephemeral{0..N}"`.
    /// 
    /// &gt; **NOTE:** Changes to `*_block_device` configuration of _existing_ resources
    /// cannot currently be detected by this provider. After updating to block device
    /// configuration, resource recreation can be manually triggered by using the
    /// [`up` command with the --replace argument](https://www.pulumi.com/docs/reference/cli/pulumi_up/).
    /// </summary>
    public partial class LaunchConfiguration : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name of the launch configuration.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Associate a public ip address with an instance in a VPC.
        /// </summary>
        [Output("associatePublicIpAddress")]
        public Output<bool?> AssociatePublicIpAddress { get; private set; } = null!;

        /// <summary>
        /// Additional EBS block devices to attach to the
        /// instance.  See Block Devices below for details.
        /// </summary>
        [Output("ebsBlockDevices")]
        public Output<ImmutableArray<Outputs.LaunchConfigurationEbsBlockDevice>> EbsBlockDevices { get; private set; } = null!;

        /// <summary>
        /// If true, the launched EC2 instance will be EBS-optimized.
        /// </summary>
        [Output("ebsOptimized")]
        public Output<bool> EbsOptimized { get; private set; } = null!;

        /// <summary>
        /// Enables/disables detailed monitoring. This is enabled by default.
        /// </summary>
        [Output("enableMonitoring")]
        public Output<bool?> EnableMonitoring { get; private set; } = null!;

        /// <summary>
        /// Customize Ephemeral (also known as
        /// "Instance Store") volumes on the instance. See Block Devices below for details.
        /// </summary>
        [Output("ephemeralBlockDevices")]
        public Output<ImmutableArray<Outputs.LaunchConfigurationEphemeralBlockDevice>> EphemeralBlockDevices { get; private set; } = null!;

        /// <summary>
        /// The name attribute of the IAM instance profile to associate
        /// with launched instances.
        /// </summary>
        [Output("iamInstanceProfile")]
        public Output<string?> IamInstanceProfile { get; private set; } = null!;

        /// <summary>
        /// The EC2 image ID to launch.
        /// </summary>
        [Output("imageId")]
        public Output<string> ImageId { get; private set; } = null!;

        /// <summary>
        /// The size of instance to launch.
        /// </summary>
        [Output("instanceType")]
        public Output<string> InstanceType { get; private set; } = null!;

        /// <summary>
        /// The key name that should be used for the instance.
        /// </summary>
        [Output("keyName")]
        public Output<string> KeyName { get; private set; } = null!;

        /// <summary>
        /// The name of the launch configuration. If you leave
        /// this blank, this provider will auto-generate a unique name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Output("namePrefix")]
        public Output<string?> NamePrefix { get; private set; } = null!;

        /// <summary>
        /// The tenancy of the instance. Valid values are
        /// `"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
        /// for more details
        /// </summary>
        [Output("placementTenancy")]
        public Output<string?> PlacementTenancy { get; private set; } = null!;

        /// <summary>
        /// Customize details about the root block
        /// device of the instance. See Block Devices below for details.
        /// </summary>
        [Output("rootBlockDevice")]
        public Output<Outputs.LaunchConfigurationRootBlockDevice> RootBlockDevice { get; private set; } = null!;

        /// <summary>
        /// A list of associated security group IDS.
        /// </summary>
        [Output("securityGroups")]
        public Output<ImmutableArray<string>> SecurityGroups { get; private set; } = null!;

        /// <summary>
        /// The maximum price to use for reserving spot instances.
        /// </summary>
        [Output("spotPrice")]
        public Output<string?> SpotPrice { get; private set; } = null!;

        /// <summary>
        /// The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
        /// </summary>
        [Output("userData")]
        public Output<string?> UserData { get; private set; } = null!;

        /// <summary>
        /// Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
        /// </summary>
        [Output("userDataBase64")]
        public Output<string?> UserDataBase64 { get; private set; } = null!;

        /// <summary>
        /// The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
        /// </summary>
        [Output("vpcClassicLinkId")]
        public Output<string?> VpcClassicLinkId { get; private set; } = null!;

        /// <summary>
        /// The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
        /// </summary>
        [Output("vpcClassicLinkSecurityGroups")]
        public Output<ImmutableArray<string>> VpcClassicLinkSecurityGroups { get; private set; } = null!;


        /// <summary>
        /// Create a LaunchConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LaunchConfiguration(string name, LaunchConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/launchConfiguration:LaunchConfiguration", name, args ?? new LaunchConfigurationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LaunchConfiguration(string name, Input<string> id, LaunchConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/launchConfiguration:LaunchConfiguration", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LaunchConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LaunchConfiguration Get(string name, Input<string> id, LaunchConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new LaunchConfiguration(name, id, state, options);
        }
    }

    public sealed class LaunchConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Associate a public ip address with an instance in a VPC.
        /// </summary>
        [Input("associatePublicIpAddress")]
        public Input<bool>? AssociatePublicIpAddress { get; set; }

        [Input("ebsBlockDevices")]
        private InputList<Inputs.LaunchConfigurationEbsBlockDeviceArgs>? _ebsBlockDevices;

        /// <summary>
        /// Additional EBS block devices to attach to the
        /// instance.  See Block Devices below for details.
        /// </summary>
        public InputList<Inputs.LaunchConfigurationEbsBlockDeviceArgs> EbsBlockDevices
        {
            get => _ebsBlockDevices ?? (_ebsBlockDevices = new InputList<Inputs.LaunchConfigurationEbsBlockDeviceArgs>());
            set => _ebsBlockDevices = value;
        }

        /// <summary>
        /// If true, the launched EC2 instance will be EBS-optimized.
        /// </summary>
        [Input("ebsOptimized")]
        public Input<bool>? EbsOptimized { get; set; }

        /// <summary>
        /// Enables/disables detailed monitoring. This is enabled by default.
        /// </summary>
        [Input("enableMonitoring")]
        public Input<bool>? EnableMonitoring { get; set; }

        [Input("ephemeralBlockDevices")]
        private InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceArgs>? _ephemeralBlockDevices;

        /// <summary>
        /// Customize Ephemeral (also known as
        /// "Instance Store") volumes on the instance. See Block Devices below for details.
        /// </summary>
        public InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceArgs> EphemeralBlockDevices
        {
            get => _ephemeralBlockDevices ?? (_ephemeralBlockDevices = new InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceArgs>());
            set => _ephemeralBlockDevices = value;
        }

        /// <summary>
        /// The name attribute of the IAM instance profile to associate
        /// with launched instances.
        /// </summary>
        [Input("iamInstanceProfile")]
        public Input<string>? IamInstanceProfile { get; set; }

        /// <summary>
        /// The EC2 image ID to launch.
        /// </summary>
        [Input("imageId", required: true)]
        public Input<string> ImageId { get; set; } = null!;

        /// <summary>
        /// The size of instance to launch.
        /// </summary>
        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// The key name that should be used for the instance.
        /// </summary>
        [Input("keyName")]
        public Input<string>? KeyName { get; set; }

        /// <summary>
        /// The name of the launch configuration. If you leave
        /// this blank, this provider will auto-generate a unique name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The tenancy of the instance. Valid values are
        /// `"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
        /// for more details
        /// </summary>
        [Input("placementTenancy")]
        public Input<string>? PlacementTenancy { get; set; }

        /// <summary>
        /// Customize details about the root block
        /// device of the instance. See Block Devices below for details.
        /// </summary>
        [Input("rootBlockDevice")]
        public Input<Inputs.LaunchConfigurationRootBlockDeviceArgs>? RootBlockDevice { get; set; }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// A list of associated security group IDS.
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// The maximum price to use for reserving spot instances.
        /// </summary>
        [Input("spotPrice")]
        public Input<string>? SpotPrice { get; set; }

        /// <summary>
        /// The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        /// <summary>
        /// Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
        /// </summary>
        [Input("userDataBase64")]
        public Input<string>? UserDataBase64 { get; set; }

        /// <summary>
        /// The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
        /// </summary>
        [Input("vpcClassicLinkId")]
        public Input<string>? VpcClassicLinkId { get; set; }

        [Input("vpcClassicLinkSecurityGroups")]
        private InputList<string>? _vpcClassicLinkSecurityGroups;

        /// <summary>
        /// The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
        /// </summary>
        public InputList<string> VpcClassicLinkSecurityGroups
        {
            get => _vpcClassicLinkSecurityGroups ?? (_vpcClassicLinkSecurityGroups = new InputList<string>());
            set => _vpcClassicLinkSecurityGroups = value;
        }

        public LaunchConfigurationArgs()
        {
        }
    }

    public sealed class LaunchConfigurationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name of the launch configuration.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Associate a public ip address with an instance in a VPC.
        /// </summary>
        [Input("associatePublicIpAddress")]
        public Input<bool>? AssociatePublicIpAddress { get; set; }

        [Input("ebsBlockDevices")]
        private InputList<Inputs.LaunchConfigurationEbsBlockDeviceGetArgs>? _ebsBlockDevices;

        /// <summary>
        /// Additional EBS block devices to attach to the
        /// instance.  See Block Devices below for details.
        /// </summary>
        public InputList<Inputs.LaunchConfigurationEbsBlockDeviceGetArgs> EbsBlockDevices
        {
            get => _ebsBlockDevices ?? (_ebsBlockDevices = new InputList<Inputs.LaunchConfigurationEbsBlockDeviceGetArgs>());
            set => _ebsBlockDevices = value;
        }

        /// <summary>
        /// If true, the launched EC2 instance will be EBS-optimized.
        /// </summary>
        [Input("ebsOptimized")]
        public Input<bool>? EbsOptimized { get; set; }

        /// <summary>
        /// Enables/disables detailed monitoring. This is enabled by default.
        /// </summary>
        [Input("enableMonitoring")]
        public Input<bool>? EnableMonitoring { get; set; }

        [Input("ephemeralBlockDevices")]
        private InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceGetArgs>? _ephemeralBlockDevices;

        /// <summary>
        /// Customize Ephemeral (also known as
        /// "Instance Store") volumes on the instance. See Block Devices below for details.
        /// </summary>
        public InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceGetArgs> EphemeralBlockDevices
        {
            get => _ephemeralBlockDevices ?? (_ephemeralBlockDevices = new InputList<Inputs.LaunchConfigurationEphemeralBlockDeviceGetArgs>());
            set => _ephemeralBlockDevices = value;
        }

        /// <summary>
        /// The name attribute of the IAM instance profile to associate
        /// with launched instances.
        /// </summary>
        [Input("iamInstanceProfile")]
        public Input<string>? IamInstanceProfile { get; set; }

        /// <summary>
        /// The EC2 image ID to launch.
        /// </summary>
        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        /// <summary>
        /// The size of instance to launch.
        /// </summary>
        [Input("instanceType")]
        public Input<string>? InstanceType { get; set; }

        /// <summary>
        /// The key name that should be used for the instance.
        /// </summary>
        [Input("keyName")]
        public Input<string>? KeyName { get; set; }

        /// <summary>
        /// The name of the launch configuration. If you leave
        /// this blank, this provider will auto-generate a unique name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The tenancy of the instance. Valid values are
        /// `"default"` or `"dedicated"`, see [AWS's Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
        /// for more details
        /// </summary>
        [Input("placementTenancy")]
        public Input<string>? PlacementTenancy { get; set; }

        /// <summary>
        /// Customize details about the root block
        /// device of the instance. See Block Devices below for details.
        /// </summary>
        [Input("rootBlockDevice")]
        public Input<Inputs.LaunchConfigurationRootBlockDeviceGetArgs>? RootBlockDevice { get; set; }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// A list of associated security group IDS.
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// The maximum price to use for reserving spot instances.
        /// </summary>
        [Input("spotPrice")]
        public Input<string>? SpotPrice { get; set; }

        /// <summary>
        /// The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        /// <summary>
        /// Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
        /// </summary>
        [Input("userDataBase64")]
        public Input<string>? UserDataBase64 { get; set; }

        /// <summary>
        /// The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
        /// </summary>
        [Input("vpcClassicLinkId")]
        public Input<string>? VpcClassicLinkId { get; set; }

        [Input("vpcClassicLinkSecurityGroups")]
        private InputList<string>? _vpcClassicLinkSecurityGroups;

        /// <summary>
        /// The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
        /// </summary>
        public InputList<string> VpcClassicLinkSecurityGroups
        {
            get => _vpcClassicLinkSecurityGroups ?? (_vpcClassicLinkSecurityGroups = new InputList<string>());
            set => _vpcClassicLinkSecurityGroups = value;
        }

        public LaunchConfigurationState()
        {
        }
    }
}
