// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.OpsWorks
{
    /// <summary>
    /// Provides an OpsWorks stack resource.
    /// </summary>
    public partial class Stack : Pulumi.CustomResource
    {
        /// <summary>
        /// If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        /// </summary>
        [Output("agentVersion")]
        public Output<string> AgentVersion { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        /// </summary>
        [Output("berkshelfVersion")]
        public Output<string?> BerkshelfVersion { get; private set; } = null!;

        /// <summary>
        /// Color to paint next to the stack's resources in the OpsWorks console.
        /// </summary>
        [Output("color")]
        public Output<string?> Color { get; private set; } = null!;

        /// <summary>
        /// Name of the configuration manager to use. Defaults to "Chef".
        /// </summary>
        [Output("configurationManagerName")]
        public Output<string?> ConfigurationManagerName { get; private set; } = null!;

        /// <summary>
        /// Version of the configuration manager to use. Defaults to "11.4".
        /// </summary>
        [Output("configurationManagerVersion")]
        public Output<string?> ConfigurationManagerVersion { get; private set; } = null!;

        /// <summary>
        /// When `use_custom_cookbooks` is set, provide this sub-object as
        /// described below.
        /// </summary>
        [Output("customCookbooksSources")]
        public Output<ImmutableArray<Outputs.StackCustomCookbooksSource>> CustomCookbooksSources { get; private set; } = null!;

        /// <summary>
        /// Custom JSON attributes to apply to the entire stack.
        /// </summary>
        [Output("customJson")]
        public Output<string?> CustomJson { get; private set; } = null!;

        /// <summary>
        /// Name of the availability zone where instances will be created
        /// by default. This is required unless you set `vpc_id`.
        /// </summary>
        [Output("defaultAvailabilityZone")]
        public Output<string> DefaultAvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The ARN of an IAM Instance Profile that created instances
        /// will have by default.
        /// </summary>
        [Output("defaultInstanceProfileArn")]
        public Output<string> DefaultInstanceProfileArn { get; private set; } = null!;

        /// <summary>
        /// Name of OS that will be installed on instances by default.
        /// </summary>
        [Output("defaultOs")]
        public Output<string?> DefaultOs { get; private set; } = null!;

        /// <summary>
        /// Name of the type of root device instances will have by default.
        /// </summary>
        [Output("defaultRootDeviceType")]
        public Output<string?> DefaultRootDeviceType { get; private set; } = null!;

        /// <summary>
        /// Name of the SSH keypair that instances will have by default.
        /// </summary>
        [Output("defaultSshKeyName")]
        public Output<string?> DefaultSshKeyName { get; private set; } = null!;

        /// <summary>
        /// Id of the subnet in which instances will be created by default. Mandatory
        /// if `vpc_id` is set, and forbidden if it isn't.
        /// </summary>
        [Output("defaultSubnetId")]
        public Output<string> DefaultSubnetId { get; private set; } = null!;

        /// <summary>
        /// Keyword representing the naming scheme that will be used for instance hostnames
        /// within this stack.
        /// </summary>
        [Output("hostnameTheme")]
        public Output<string?> HostnameTheme { get; private set; } = null!;

        /// <summary>
        /// Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        /// </summary>
        [Output("manageBerkshelf")]
        public Output<bool?> ManageBerkshelf { get; private set; } = null!;

        /// <summary>
        /// The name of the stack.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the region where the stack will exist.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The ARN of an IAM role that the OpsWorks service will act as.
        /// </summary>
        [Output("serviceRoleArn")]
        public Output<string> ServiceRoleArn { get; private set; } = null!;

        [Output("stackEndpoint")]
        public Output<string> StackEndpoint { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Boolean value controlling whether the custom cookbook settings are
        /// enabled.
        /// </summary>
        [Output("useCustomCookbooks")]
        public Output<bool?> UseCustomCookbooks { get; private set; } = null!;

        /// <summary>
        /// Boolean value controlling whether the standard OpsWorks
        /// security groups apply to created instances.
        /// </summary>
        [Output("useOpsworksSecurityGroups")]
        public Output<bool?> UseOpsworksSecurityGroups { get; private set; } = null!;

        /// <summary>
        /// The id of the VPC that this stack belongs to.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Stack resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Stack(string name, StackArgs args, CustomResourceOptions? options = null)
            : base("aws:opsworks/stack:Stack", name, args ?? new StackArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Stack(string name, Input<string> id, StackState? state = null, CustomResourceOptions? options = null)
            : base("aws:opsworks/stack:Stack", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Stack resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Stack Get(string name, Input<string> id, StackState? state = null, CustomResourceOptions? options = null)
        {
            return new Stack(name, id, state, options);
        }
    }

    public sealed class StackArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        /// </summary>
        [Input("agentVersion")]
        public Input<string>? AgentVersion { get; set; }

        /// <summary>
        /// If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        /// </summary>
        [Input("berkshelfVersion")]
        public Input<string>? BerkshelfVersion { get; set; }

        /// <summary>
        /// Color to paint next to the stack's resources in the OpsWorks console.
        /// </summary>
        [Input("color")]
        public Input<string>? Color { get; set; }

        /// <summary>
        /// Name of the configuration manager to use. Defaults to "Chef".
        /// </summary>
        [Input("configurationManagerName")]
        public Input<string>? ConfigurationManagerName { get; set; }

        /// <summary>
        /// Version of the configuration manager to use. Defaults to "11.4".
        /// </summary>
        [Input("configurationManagerVersion")]
        public Input<string>? ConfigurationManagerVersion { get; set; }

        [Input("customCookbooksSources")]
        private InputList<Inputs.StackCustomCookbooksSourceArgs>? _customCookbooksSources;

        /// <summary>
        /// When `use_custom_cookbooks` is set, provide this sub-object as
        /// described below.
        /// </summary>
        public InputList<Inputs.StackCustomCookbooksSourceArgs> CustomCookbooksSources
        {
            get => _customCookbooksSources ?? (_customCookbooksSources = new InputList<Inputs.StackCustomCookbooksSourceArgs>());
            set => _customCookbooksSources = value;
        }

        /// <summary>
        /// Custom JSON attributes to apply to the entire stack.
        /// </summary>
        [Input("customJson")]
        public Input<string>? CustomJson { get; set; }

        /// <summary>
        /// Name of the availability zone where instances will be created
        /// by default. This is required unless you set `vpc_id`.
        /// </summary>
        [Input("defaultAvailabilityZone")]
        public Input<string>? DefaultAvailabilityZone { get; set; }

        /// <summary>
        /// The ARN of an IAM Instance Profile that created instances
        /// will have by default.
        /// </summary>
        [Input("defaultInstanceProfileArn", required: true)]
        public Input<string> DefaultInstanceProfileArn { get; set; } = null!;

        /// <summary>
        /// Name of OS that will be installed on instances by default.
        /// </summary>
        [Input("defaultOs")]
        public Input<string>? DefaultOs { get; set; }

        /// <summary>
        /// Name of the type of root device instances will have by default.
        /// </summary>
        [Input("defaultRootDeviceType")]
        public Input<string>? DefaultRootDeviceType { get; set; }

        /// <summary>
        /// Name of the SSH keypair that instances will have by default.
        /// </summary>
        [Input("defaultSshKeyName")]
        public Input<string>? DefaultSshKeyName { get; set; }

        /// <summary>
        /// Id of the subnet in which instances will be created by default. Mandatory
        /// if `vpc_id` is set, and forbidden if it isn't.
        /// </summary>
        [Input("defaultSubnetId")]
        public Input<string>? DefaultSubnetId { get; set; }

        /// <summary>
        /// Keyword representing the naming scheme that will be used for instance hostnames
        /// within this stack.
        /// </summary>
        [Input("hostnameTheme")]
        public Input<string>? HostnameTheme { get; set; }

        /// <summary>
        /// Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        /// </summary>
        [Input("manageBerkshelf")]
        public Input<bool>? ManageBerkshelf { get; set; }

        /// <summary>
        /// The name of the stack.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the region where the stack will exist.
        /// </summary>
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        /// <summary>
        /// The ARN of an IAM role that the OpsWorks service will act as.
        /// </summary>
        [Input("serviceRoleArn", required: true)]
        public Input<string> ServiceRoleArn { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Boolean value controlling whether the custom cookbook settings are
        /// enabled.
        /// </summary>
        [Input("useCustomCookbooks")]
        public Input<bool>? UseCustomCookbooks { get; set; }

        /// <summary>
        /// Boolean value controlling whether the standard OpsWorks
        /// security groups apply to created instances.
        /// </summary>
        [Input("useOpsworksSecurityGroups")]
        public Input<bool>? UseOpsworksSecurityGroups { get; set; }

        /// <summary>
        /// The id of the VPC that this stack belongs to.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public StackArgs()
        {
        }
    }

    public sealed class StackState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        /// </summary>
        [Input("agentVersion")]
        public Input<string>? AgentVersion { get; set; }

        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        /// </summary>
        [Input("berkshelfVersion")]
        public Input<string>? BerkshelfVersion { get; set; }

        /// <summary>
        /// Color to paint next to the stack's resources in the OpsWorks console.
        /// </summary>
        [Input("color")]
        public Input<string>? Color { get; set; }

        /// <summary>
        /// Name of the configuration manager to use. Defaults to "Chef".
        /// </summary>
        [Input("configurationManagerName")]
        public Input<string>? ConfigurationManagerName { get; set; }

        /// <summary>
        /// Version of the configuration manager to use. Defaults to "11.4".
        /// </summary>
        [Input("configurationManagerVersion")]
        public Input<string>? ConfigurationManagerVersion { get; set; }

        [Input("customCookbooksSources")]
        private InputList<Inputs.StackCustomCookbooksSourceGetArgs>? _customCookbooksSources;

        /// <summary>
        /// When `use_custom_cookbooks` is set, provide this sub-object as
        /// described below.
        /// </summary>
        public InputList<Inputs.StackCustomCookbooksSourceGetArgs> CustomCookbooksSources
        {
            get => _customCookbooksSources ?? (_customCookbooksSources = new InputList<Inputs.StackCustomCookbooksSourceGetArgs>());
            set => _customCookbooksSources = value;
        }

        /// <summary>
        /// Custom JSON attributes to apply to the entire stack.
        /// </summary>
        [Input("customJson")]
        public Input<string>? CustomJson { get; set; }

        /// <summary>
        /// Name of the availability zone where instances will be created
        /// by default. This is required unless you set `vpc_id`.
        /// </summary>
        [Input("defaultAvailabilityZone")]
        public Input<string>? DefaultAvailabilityZone { get; set; }

        /// <summary>
        /// The ARN of an IAM Instance Profile that created instances
        /// will have by default.
        /// </summary>
        [Input("defaultInstanceProfileArn")]
        public Input<string>? DefaultInstanceProfileArn { get; set; }

        /// <summary>
        /// Name of OS that will be installed on instances by default.
        /// </summary>
        [Input("defaultOs")]
        public Input<string>? DefaultOs { get; set; }

        /// <summary>
        /// Name of the type of root device instances will have by default.
        /// </summary>
        [Input("defaultRootDeviceType")]
        public Input<string>? DefaultRootDeviceType { get; set; }

        /// <summary>
        /// Name of the SSH keypair that instances will have by default.
        /// </summary>
        [Input("defaultSshKeyName")]
        public Input<string>? DefaultSshKeyName { get; set; }

        /// <summary>
        /// Id of the subnet in which instances will be created by default. Mandatory
        /// if `vpc_id` is set, and forbidden if it isn't.
        /// </summary>
        [Input("defaultSubnetId")]
        public Input<string>? DefaultSubnetId { get; set; }

        /// <summary>
        /// Keyword representing the naming scheme that will be used for instance hostnames
        /// within this stack.
        /// </summary>
        [Input("hostnameTheme")]
        public Input<string>? HostnameTheme { get; set; }

        /// <summary>
        /// Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        /// </summary>
        [Input("manageBerkshelf")]
        public Input<bool>? ManageBerkshelf { get; set; }

        /// <summary>
        /// The name of the stack.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the region where the stack will exist.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ARN of an IAM role that the OpsWorks service will act as.
        /// </summary>
        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        [Input("stackEndpoint")]
        public Input<string>? StackEndpoint { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// Boolean value controlling whether the custom cookbook settings are
        /// enabled.
        /// </summary>
        [Input("useCustomCookbooks")]
        public Input<bool>? UseCustomCookbooks { get; set; }

        /// <summary>
        /// Boolean value controlling whether the standard OpsWorks
        /// security groups apply to created instances.
        /// </summary>
        [Input("useOpsworksSecurityGroups")]
        public Input<bool>? UseOpsworksSecurityGroups { get; set; }

        /// <summary>
        /// The id of the VPC that this stack belongs to.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public StackState()
        {
        }
    }
}
